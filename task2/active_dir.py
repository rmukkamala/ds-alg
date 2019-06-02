
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)
        
    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    group_list=list()
    results=list()
    group_list=group.get_groups()
    if len(group_list) > 0:
        for entry in group_list:
            results.append(is_user_in_group(user, entry))
    if True in results:
        return True
    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
grand_child = Group("grandchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
child.add_group(grand_child)
parent.add_group(child)

grand_child.add_user("jack")
child.add_user("rohan")
child.add_user("tony")

##Test Cases

print(is_user_in_group("rohan",parent)) ##True
print(is_user_in_group("tony",sub_child))  ##True
print(is_user_in_group("tony",parent)) ##True
print(is_user_in_group("mike",parent))  ##False
print(is_user_in_group("joel",parent))  ##False
print(is_user_in_group("jack",parent))  ##False