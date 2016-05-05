from os import path


def _read_file(file_path):
	if path.isfile(file_path):
		with open(file_path, "r") as file:
			content = file.read()
			file.close()
			return content
	else:
		return None


def get_private_key(base_path, consumer):
	key_path = path.join(base_path, "priv_{}.pem".format(consumer))
	return _read_file(key_path)


def get_public_key(base_path, consumer):
	key_path = path.join(base_path, "pub_{}.pem".format(consumer))
	return _read_file(key_path)