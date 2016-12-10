"""
lib.Command
"""

class Command(object):
    """
    Command line parser and validator
    """

    ARGS = {
        'C': [('width', int), ('height', int)],
        'L': [('x1', int), ('y1', int), ('x2', int), ('y2', int)],
        'R': [('x1', int), ('y1', int), ('x2', int), ('y2', int)],
        'B': [('x1', int), ('y1', int), ('c', str)],
        'Q': []
    }

    ERROR = '0'
    ERROR_REASON = 'reason'
    REASON_COORD_RANGE = 'range'
    REASON_ARG_TYPE = 'type'
    REASON_ARG_MISSING = 'missing'

    @staticmethod
    def parse(command_line, x_max, y_max):
        """
        Parses and validates the given command line
        Returns a dictionary containing the command verb and its arguments

        Parameters
        ----------
        command_line : str
            The unparsed command text string
        x_max : int
            Maximum value for all 'y' coordinates
        y_max : int
            Maximum value for all 'x' coordinates

        Returns
        -------
        dictionary
            Parsed & validated command arguments OR
            error status if parsing or validation failied
        """
        parsed_command = {'verb': Command.ERROR}
        command_args = command_line.split()

        if len(command_args) > 0:
            verb = command_args[0].upper()

            if verb in Command.ARGS:
                for i, (arg_name, dtype) in enumerate(Command.ARGS[verb]):
                    try:
                        arg_val = dtype(command_args[i + 1])
                    except ValueError:
                        # Invalid argument data type
                        parsed_command[Command.ERROR_REASON] = Command.REASON_ARG_TYPE
                        return parsed_command
                    except IndexError:
                        # Argument missing
                        parsed_command[Command.ERROR_REASON] = Command.REASON_ARG_MISSING
                        return parsed_command

                    if (arg_name[0] == 'x' and not 1 <= arg_val <= x_max) or \
                        (arg_name[0] == 'y' and not 1 <= arg_val <= y_max):
                        parsed_command[Command.ERROR_REASON] = Command.REASON_COORD_RANGE
                        return parsed_command

                    if arg_name[0] == 'c' and len(arg_val) != 1:
                        parsed_command[Command.ERROR_REASON] = Command.REASON_ARG_TYPE
                        return parsed_command

                    parsed_command[arg_name] = arg_val

                parsed_command['verb'] = verb

        return parsed_command
