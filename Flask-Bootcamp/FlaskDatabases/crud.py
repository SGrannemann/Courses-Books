from basic import db, Puppy

# Create

my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

# Read
all_puppies = Puppy.query.all()  # list of objects on the puppies table
# select by ID
puppy_one = Puppy.query.get(1)

puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())

# Update

first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()


# Delete
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)
