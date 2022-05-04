def remove_alphas(target):
  ## remove characters
  alphas = [chr(char) for char in range(65, 91)] + [chr(char) for char in range(97, 123)] # create a list containing upper and lower case alphabets 
  for alpha in alphas:
    try:
      target.remove(alpha) # remove alphabets of the vocab list
    except:
      pass

def to_lower(vocabs):
  for index in range(0, len(vocabs)):
    if not vocabs[index].isupper() and not vocabs[index].islower(): # find if the vocab is a mixed type, which contains upper and lower case
      vocabs[index] = vocabs[index].lower() # convert the vocab into lower case
  return vocabs