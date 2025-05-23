import json

import pyperclip

from . import editor, parser, printer, selector


def handle_use_command(args, content):
    if args.subcommand == "rand":
        try:
            name = selector.select_random_unused(content)
            updated_content = editor.mark_as_checked(content, name)
            args.path.write_text(updated_content)
            if args.out == "json":
                print(json.dumps({"name": name}))
            else:
                print(name)
            pyperclip.copy(name)
        except selector.NoUnusedNamesError as e:
            if args.out == "json":
                print(json.dumps({"error": str(e)}))
            else:
                print(f"Error: {e}")
        return
    elif args.subcommand == "check":
        updated_content = editor.mark_as_checked(content, args.name)
        args.path.write_text(updated_content)
        if args.out == "json":
            print(json.dumps({"message": f"Marked '{args.name}' as checked"}))
        else:
            print(f"Marked '{args.name}' as checked")
        parser.parse_markdown(updated_content)
    else:
        print("Please specify a subcommand: check or rand")


def handle_get_command(args, content):
    parsed_data = parser.parse_markdown(content)
    if args.subcommand == "used":
        printer.print_used_names(parsed_data, args.out)
    elif args.subcommand == "unused":
        printer.print_unused_names(parsed_data, args.out)
    elif args.subcommand == "all":
        printer.print_all_names(parsed_data, args.out)
    elif args.subcommand == "rand":
        try:
            name = selector.select_random_unused(content)
            if args.out == "json":
                print(json.dumps({"name": name}))
            else:
                print(name)
            pyperclip.copy(name)
        except selector.NoUnusedNamesError as e:
            if args.out == "json":
                print(json.dumps({"error": str(e)}))
            else:
                print(f"Error: {e}")
    else:
        print("Please specify a subcommand: used, unused, all, or rand")
