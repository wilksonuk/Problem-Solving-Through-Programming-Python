# If the parameter plan has the value "jumping over" then the message "We cannot escape that way! The boulder is too big!" should be displayed.
# Otherwise, if the parameter plan has the value "running around" then the message "We cannot escape that way! The boulder is moving too fast!" should be displayed.
# Otherwise, if the parameter plan has the value "cross bridge ahead" then the message "That might just work! Let's go!" should be displayed.
# Otherwise the message "We cannot escape that way! The boulder is in the way!" should be displayed.
# Finally, the program should contain three calls to your escape function as follows:
def escape(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way! The boulder is in the way!")

escape("jumping over")
escape("running around")
escape("cross bridge ahead")