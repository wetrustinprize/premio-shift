from premioshift.shifter import shift_message

import argparse

if __name__ == "__main__":
    # arguments
    parser = argparse.ArgumentParser()
    requiredNamed = parser.add_argument_group('required named arguments')

    requiredNamed.add_argument("-m", "--message", help="Message", type=str, required=True)
    requiredNamed.add_argument("-k", "--key", help="Shift key", type=str, required=True)

    parser.add_argument("-s", "--shift", help="Total shift steps", type=int, default=0)
    parser.add_argument("-p", "--pos", help="Message initial shift", type=int, default=0)
    parser.add_argument("-t", "--to", help="Move steps to this shift", type=int, default=0)

    args = parser.parse_args()

    # shift message
    print(shift_message(args.message, args.key, shift_to=args.to, cur_pos=args.pos, shift=args.shift))