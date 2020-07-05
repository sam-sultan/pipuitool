

import pip

from subprocess import Popen, PIPE
import json


class PIP:

	def __init__(self):
		pass

	def install(self, packages):

		p = Popen(["pip", "install"]+packages, stdin=PIPE, stdout=PIPE, stderr=PIPE)
		output, err = p.communicate(b"input data that is passed to subprocess' stdin")

		return output if p.returncode == 0 else err

	def remove(self, packages):

		p = Popen(["pip", "uninstall", "-y"]+packages, stdin=PIPE, stdout=PIPE, stderr=PIPE)
		output, err = p.communicate(b"input data that is passed to subprocess' stdin")

		return output if p.returncode == 0 else err

	def list(self):

		p = Popen(["pip", "list", "--format", "json"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
		output, err = p.communicate(b"input data that is passed to subprocess' stdin")

		return json.loads(output) if p.returncode == 0 else []

	def has(self, package):

		return len(list(filter(lambda x: x['name'] == package, self.list()))) > 0


def main():
    print(PIP().list())
    
if __name__ == '__main__':
    main()
	