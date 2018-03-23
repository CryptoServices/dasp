from jinja2 import Template, Environment, FileSystemLoader
import json

vulnList = [
	['Reentrancy', 'reentrancy.html'], # DAO
	['Access Control', 'access_control.html'], # Parity
	['Arithmetic', 'arithmetic.html'], 
	['Unchecked Low Level Calls', 'unchecked_low_level_calls.html'],
	['Denial of Services', 'dos.html'],
	['Bad Randomness', 'bad_randomness.html'],
	['Front Running', 'front_running.html'],
	['Time Manipulation', 'time_manipulation.html'],
	['Short Addresses', 'short_addresses.html'],
	['Unknown Unknowns', 'unknown.html'],
]

def main():

	# retrieve vulnerabilities
	for rank, vuln in enumerate(vulnList):
		ff = open('./findings/' + vuln[1])
		tt = Template(ff.read())
		vulnList[rank][1] = tt.render(num=rank+1)
		ff.close()

	# main template
	tt = Environment(loader=FileSystemLoader('findings/')).from_string(open('./findings/home.html').read())
	toWrite = tt.render(vulnList=vulnList)
	open('./dist/index.html', 'w').write(toWrite)

	# timeline
	tt = Environment(loader=FileSystemLoader('findings/')).from_string(open('./findings/timeline.html').read())

	vulns = json.load(open('./findings/timeline.json'))
	toWrite = tt.render(vulns=vulns)
	open('./dist/timeline.html', 'w').write(toWrite)

if __name__ == "__main__":
	main()