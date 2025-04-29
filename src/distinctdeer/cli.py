from . import commands, parser_config


def main() -> None:
    args = parser_config.get_args()
    try:
        content = args.path.read_text()
        if args.command == "use":
            commands.handle_use_command(args, content)
        elif args.command == "get":
            commands.handle_get_command(args, content)
        else:
            print("Please specify a command: get or use")
    except FileNotFoundError:
        print(f"Error: File not found at {args.path}")
    except Exception as e:
        print(f"Error: {e}")
