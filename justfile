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
