set shell := ["bash", "-cu"]

# Create a skill from templates/skill under skills/<path>.
add-skill skill_path:
    #!/usr/bin/env bash
    set -euo pipefail

    if [[ ! "{{ skill_path }}" =~ ^[a-z0-9][a-z0-9-]*(/[a-z0-9][a-z0-9-]*)*$ ]]; then
      echo "error: skill path must contain lowercase letters, numbers, and hyphens (for example: newsletter/medium-custom)" >&2
      exit 2
    fi

    target="skills/{{ skill_path }}"
    if [[ -e "$target" ]]; then
      echo "error: $target already exists" >&2
      exit 3
    fi

    mkdir -p "$(dirname "$target")"
    cp -R templates/skill "$target"

    skill_name="{{ skill_path }}"
    skill_name="${skill_name##*/}"

    for metadata_file in "$target/SKILL.md" "$target/agents/openai.yaml"; do
      awk -v skill_name="$skill_name" '
        $0 == "name: replace-with-skill-name" { $0 = "name: " skill_name }
        { gsub(/\$replace-with-skill-name/, "$" skill_name); print }
      ' "$metadata_file" > "$metadata_file.tmp"
      mv "$metadata_file.tmp" "$metadata_file"
    done

    echo "Created $target"

# Lift and shift one complete staged skill folder into skills/<target-parent>.
migrate-skill source_name target_parent:
    #!/usr/bin/env bash
    set -euo pipefail

    if [[ ! "{{ source_name }}" =~ ^[a-z0-9][a-z0-9-]*$ ]]; then
      echo "error: source name must be one lowercase, hyphenated folder name" >&2
      exit 2
    fi
    if [[ ! "{{ target_parent }}" =~ ^[a-z0-9][a-z0-9-]*(/[a-z0-9][a-z0-9-]*)*$ ]]; then
      echo "error: target parent must be a relative path below skills/" >&2
      exit 2
    fi

    source="migrate_skills/{{ source_name }}"
    target="skills/{{ target_parent }}/{{ source_name }}"

    if [[ ! -d "$source" ]]; then
      echo "error: source directory does not exist: $source" >&2
      exit 3
    fi
    if [[ ! -f "$source/SKILL.md" ]]; then
      echo "error: source package has no SKILL.md: $source" >&2
      exit 4
    fi
    if [[ -e "$target" ]]; then
      echo "error: target already exists: $target" >&2
      exit 5
    fi

    declared_name="$({ ruby -ryaml -e '
      text = File.read(ARGV.fetch(0))
      parts = text.split(/^---\s*$\n?/, 3)
      abort "SKILL.md must begin with YAML frontmatter" unless parts.length == 3 && parts[0].strip.empty?
      data = YAML.safe_load(parts[1]) || {}
      name = data["name"]
      abort "SKILL.md frontmatter requires name" unless name.is_a?(String) && !name.empty?
      print name
    ' "$source/SKILL.md"; } 2>&1)" || {
      echo "error: $declared_name" >&2
      exit 6
    }

    if [[ "$declared_name" != "{{ source_name }}" ]]; then
      echo "error: folder name '{{ source_name }}' does not match SKILL.md name '$declared_name'" >&2
      exit 7
    fi

    mkdir -p "$(dirname "$target")"
    cp -R "$source" "$target"

    if ! diff -qr "$source" "$target" >/dev/null; then
      echo "error: copied package differs from source; removing incomplete target" >&2
      find "$target" -depth -delete
      exit 8
    fi

    find "$source" -depth -delete
    echo "Migrated $source -> $target"

# Migrate every complete skill package listed in migrate_skills/mapper.yaml.
migrate-skills:
    #!/usr/bin/env bash
    set -euo pipefail

    mapper_output="$(ruby -ryaml -e '
      entries = YAML.safe_load(File.read(ARGV.fetch(0))) || []
      abort "mapper must be a YAML sequence" unless entries.is_a?(Array)
      entries.each do |entry|
        abort "each mapper item must contain exactly one source: target pair" unless entry.is_a?(Hash) && entry.length == 1
        source, target = entry.first
        abort "mapper source and target must be strings" unless source.is_a?(String) && target.is_a?(String)
        puts "#{source}\t#{target}"
      end
    ' migrate_skills/mapper.yaml)"

    if [[ -z "$mapper_output" ]]; then
      echo "No skills are mapped in migrate_skills/mapper.yaml"
      exit 0
    fi

    while IFS= read -r mapping; do
      IFS=$'\t' read -r source_name target_parent <<< "$mapping"
      just migrate-skill "$source_name" "$target_parent"
    done <<< "$mapper_output"
