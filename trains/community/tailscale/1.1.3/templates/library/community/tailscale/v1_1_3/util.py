from base_v1_0_1 import utils


def get_args(data):
    args = []

    if data.get("advertise_exit_node"):
        args.append("--advertise-exit-node")

    reserved_keys = ["--advertise-exit-node", "--hostname"]
    for arg in data.get("extra_args", []):
        for key in reserved_keys:
            if arg.startswith(key):
                utils.throw_error(f"Please use the dedicated field for {key}")
        args.append(arg)
    return " ".join(args)