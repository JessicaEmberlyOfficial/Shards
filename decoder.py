import os
def decode():
  os.system("clear")
  decode = input("What should I decode?: ")
  sentence = decode.replace("|_|", "a").replace("|-|", "b").replace("*", "c").replace("/|", "d").replace("-+-", "e").replace("|||", "f").replace('""', "g").replace('"', "h").replace("#", "i").replace("/–-", "j").replace("]_[", "k").replace("•", "l").replace("~", "m").replace("()+()", "n").replace("00", "o").replace("!;!", "p").replace("@,", "q").replace("+-+", "r").replace("?,?", "s").replace("!!!-!!!", "t").replace("()", "u").replace("€£", "v").replace("Vn", "w").replace("'›", "x").replace("‹›", "y").replace("0", "z")
  os.system("clear")
  print(sentence)