# Epicore sample
import engine as ec

# Initialize the game engine and loadbar
ec.epc.init('Test Game', "1.0.0", "A test game", "Epicore")
ec.epc.loadbar()
print("\n")

# I found this trivia question online
ec.epc.new_question("What does CODA stand for? ", "Child of Deaf Adults", "print('Correct')", "print('False')")