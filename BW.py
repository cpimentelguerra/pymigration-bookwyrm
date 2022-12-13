import pandas as pd


BW = pd.read_csv('BW.csv')

BW.rename(columns = {'title':'Title', 'author_text':'Author', 'isbn_10':'ISBN', 'isbn_13':'ISBN13', 'rating':'My Rating', 'review_cw':'Spoiler', 'review_content':'My Review'}, inplace = True)

BW.drop('remote_id', axis=1, inplace=True)
BW.drop('openlibrary_key', axis=1, inplace=True)
BW.drop('inventaire_id', axis=1, inplace=True)
BW.drop('librarything_key', axis=1, inplace=True)
BW.drop('goodreads_key', axis=1, inplace=True)
BW.drop('bnf_id', axis=1, inplace=True)
BW.drop('viaf', axis=1, inplace=True)
BW.drop('wikidata', axis=1, inplace=True)
BW.drop('asin', axis=1, inplace=True)
BW.drop('oclc_number', axis=1, inplace=True)
BW.drop('review_name', axis=1, inplace=True)

column_to_move = BW.pop("Spoiler")

# insert column with insert(location, column_name, column_value)

BW.insert(6, "Spoiler", column_to_move)

BW.insert(0, 'Book Id', "")
BW.insert(3, 'Author l-f', "")
BW.insert(4, 'Additional Authors', "")
BW.insert(8, 'Average Rating', "")
BW.insert(9, 'Publisher', "")
BW.insert(10, 'Binding', "")
BW.insert(11, 'Number of Pages', "")
BW.insert(12, 'Year Published', "")
BW.insert(13, 'Original Publication Year', "")
BW.insert(14, 'Date Read', "")
BW.insert(15, 'Date Added', "")
BW.insert(16, 'Bookshelves', "")
BW.insert(17, 'Bookshelves with positions', "")
BW.insert(18, 'Exclusive Shelf', "to-read")
BW.insert(21, 'Private Notes', "")
BW.insert(22, 'Read Count', "")
BW.insert(23, 'Owned Copies', "")

BW.loc[BW['My Rating'] > 0, 'Exclusive Shelf'] = 'read'
BW.loc[BW['My Rating'] > 0, 'Date Read'] = '2022/12/06'

BW.to_csv('BWnew.csv', index=False)