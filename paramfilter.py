import argparse
from include import filterer,browseResults
import datetime


parser = argparse.ArgumentParser(description="ParamLinter")
parser.add_argument("-p","--path", help="Path to the file containing the urls to filter",required=True)
parser.add_argument("-f","--fuzz", help="fuzz text",required=True)
parser.add_argument("-hti","--htmli", help="[Y/N] filter possible html injections",default=False)
parser.add_argument("-h","--help", help="help",default=False)
args = parser.parse_args()

file = open(args.path, "r")
success = []
i = 0
for line in file:
    if i > 199:
        break
    line = line.strip()
    if line.startswith("http"):
        # continue to checking
        if filterer.Filterer(line, fuzzText=args.fuzz).get_data():
            success.append(line)
    else:
        # add "http://" to the line and then send to the checking
        if filterer("http://" + line).get_data():
            success.append("http://" + line)
    i += 1

now = datetime.datetime.now()
outputFile = open(f"results/output_{now.strftime('%Y_%m_%d %H_%M_%S')}.txt", "a")
for line in success:
    outputFile.write(line + "\n")

file.close()
outputFile.close()

askSelenuim = input("Would you like to the successful results in the browser? [Y/N]: ")
if askSelenuim.lower() == "y":
    pass