"""Change excel files with extension 'xls' to tsv files."""

from bs4 import BeautifulSoup
import io
import os
import pandas as pd
import sys


def change_files_from_dir(src_path, dest_relative_path=None):
	old_path = os.getcwd()
	try:
		os.chdir(src_path)
	except:
		raise OSError("That source doesn't exist")
	else:
		file_lists = os.listdir()

	for file_name in file_lists:
		try:
			name, extension = os.path.splitext(file_name)
			if dest_relative_path:
				tsv_name = os.path.join(dest_relative_path, name + '.tsv')
				csv_name = os.path.join(dest_relative_path, name + '.csv')
			else:
				tsv_name = name + '.tsv'
				csv_name = name + '.csv'

			if extension in ['.xls', '.xlsx']:
				# print '%s started!' % csv_name
				print("{} started!".format(csv_name))
				text = open(file_name, encoding="utf-8").read()
				# text = io.open(file_name, encoding="utf-8").read()
			else:
				continue

			text = text.replace('\n', '')
			text = text.replace('\t', '')

			with open(tsv_name, 'w', encoding="utf-8") as fd:
			# with io.open(tsv_name, 'w', encoding="utf-8") as fd:
				parsed_text = BeautifulSoup(text, 'html.parser')
				all_trs = parsed_text.find_all('tr')[:-1]
				for i, tr in enumerate(all_trs):
					newline = ''
					for td in tr.find_all('td' if i != 0 else 'th'):
						newline += td.text if td.text else '.'
						newline += '\t'
					newline = newline[:-1]
					newline += '\n'
					fd.write(newline)

			file = pd.read_csv(tsv_name, sep='\t')
			file.to_csv(csv_name, index=False, index_label=False)
			os.remove(tsv_name)
		except:
			print("!!!!!!!!!!!!!!!!!!!!!!!! Cannot make {}".format(csv_name))
			# print("!!!!!!!!!!!!!!!!!!!!!!!! Cannot make %s" % csv_name)

	os.chdir(old_path)


if __name__ == '__main__':
	src_path, dest_path = sys.argv[1], sys.argv[2]
	change_files_from_dir(src_path, dest_path)