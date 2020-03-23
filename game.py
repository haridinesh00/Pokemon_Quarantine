# Create the database when the game starts
from createDb import createDatabase
createDatabase()

# Create objects of 2 trainers
from trainer import Trainer

trainer1 = Trainer()
trainer2 = Trainer()


# TO DO (v1)
# Select Pokemon from database
# Create function for fight
# Faint pkmn on 0 hp 
