def generate_invitations(template, attendees):
    # Check the type of the template
    if not isinstance(template, str):
        print(f"Error: Template should be a string (str), but got {type(template).__name__}")
        return

    # Check that attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Attendees should be a list of dictionaries, but got {type(attendees).__name__}")
        return

    # Check if the template is empty
    if template.strip() == "":
        print("Template is empty, no files were generated.")
        return

    # Check if the attendees list is empty
    if len(attendees) == 0:
        print("No data provided, no files were generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    # Iterate over each attendee and replace placeholders with values
    for idx, attendee in enumerate(attendees, start=1):
        output_content = template

        for ph in placeholders:
            value = attendee.get(ph)
            if value is None:
                value = "N/A"
            output_content = output_content.replace(f"{{{ph}}}", str(value))

        filename = f"output_{idx}.txt"
        try:
            with open(filename, "w") as f:
                f.write(output_content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            continue
