def build_user_message(parsed_data, machine_name, extra_context):
    parts = []

    if machine_name:
        parts.append(f"Machine / System: {machine_name}")

    if extra_context:
        parts.append(f"Additional context: {extra_context}")

    parts.append("Data / Logs:")
    parts.append(parsed_data)

    return "\n\n".join(parts)