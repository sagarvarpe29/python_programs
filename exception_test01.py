
def main():
    acronyms = {'LOL': 'laugh out loud',
            'IDK': 'I dont know',
            'TBH': 'to be honest'}

    try:
        definition = acronyms['BTW']
    except:
        print('The key does not exist')
    finally:
        print('The acronyms we have are:')
        for acronym in acronyms:
            print(acronym)
    print('The program keep on going...')

main()