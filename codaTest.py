from codaio import Coda, Document
# Initialize by providing a coda object directly
coda = Coda('5335e58b-1d04-474a-ab86-df2ec848ae9c')

doc = Document('memex', coda=coda)

#doc.list_tables()