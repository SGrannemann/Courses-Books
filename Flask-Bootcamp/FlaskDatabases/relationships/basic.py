from models import db, Puppy, Owner, Toy


# create puppies
rufus = Puppy('Rufus')
fido = Puppy('Fido')


# add puppies to db
db.session.add_all([rufus, fido])
db.session.commit()
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
# Create owner

jose = Owner('Jose', rufus.id)

# give rufus toys
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)
db.session.add_all([jose, toy1, toy2])
db.session.commit()

# grab rufus after additions

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
rufus.report_toys()
