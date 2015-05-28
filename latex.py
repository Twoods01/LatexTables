import sys, csv

def main(args):

	if len(args) != 1:
		print("Please include a single target csv file")
		return


	print("Taking data from " + args[0])

	latex = open("latex.txt", 'wb')
	latex.write("\\begin{table}[h] \n")
	

	with open(args[0], 'rb') as csvfile:
		reader = csv.reader(csvfile)

		for i, row in enumerate(reader):
			if i == 0:
				latex.write("\\begin{tabular}{" + 'l'*len(row) + "} \n")

			string = " & ".join(row)


			latex.write(string + "\\\\\n")

	latex.write("\\end{tabular}\n")
	latex.write("\\end{table}\n")
	latex.close()

if __name__ == '__main__':
    main(sys.argv[1:])