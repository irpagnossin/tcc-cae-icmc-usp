import csv


COMPONENTS = [(15,19), (16,20), (17,21), (18,22)]

with open('output-desafio-4.csv', 'w') as output:
	writer = csv.writer(output, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	writer.writerow(['turma', 'date', 'student', 'satisfaction', 'pace', 'relevance', 'component', 'learn'])

	with open('anonymized_dataset.csv', 'r') as f:
		reader = csv.reader(f, delimiter=';', quotechar='"')

		for row_idx, row in enumerate(reader):

			if row_idx == 0 or row[3] == '':
				continue

			id = row[1:7]

			for component_id, result in COMPONENTS:
				if not row[component_id] == '':
					writer.writerow(id + [row[component_id], row[result]])