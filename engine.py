import loadbar, scripting

class epc:
  def init(gname, gver, gdesc, gauth):
    print("Epicore Game Engine Initiaized")
    print(f"Game: {gname}\nVersion: {gver}\nDescription: {gdesc}\nAuthor: {gauth}")

  def loadbar():
    loadbar.loading_bar()

  def load_script(self, pyfile):
    try:
        with open(pyfile, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"
    exec(code)

  def load_ec_script(script):
    scripting.exec(script)

  def new_question(question, answer, next_func_correct, next_func_incorrect):
    ask = input(question)
    if question == answer:
      next_func_correct
    else:
      next_func_incorrect
