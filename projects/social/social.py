import random

class User:
    def __init__(self, name):
        self.name = name


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f'User {i + 1}')

        # Create friendships
        potential_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                potential_friendships.append((user_id, friend_id))

        random.shuffle(potential_friendships)

        total_friendships = num_users * avg_friendships // 2
        random_friendships = potential_friendships[:total_friendships]

        counter = 0
        for friendship in random_friendships:
            counter += 1
            self.add_friendship(friendship[0], friendship[1])
    
    def populate_graph_stretch(self, num_users, avg_friendships):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        for i in range(num_users):
            self.add_user(f'User {i + 1}')

        total_friendships = num_users * avg_friendships // 2
        friendships_added = 0

        while friendships_added < total_friendships:
            user_a = random.randint(1, num_users)
            user_b = random.randint(1, num_users)
            if self.add_friendship(user_a, user_b):
                friendships_added += 1

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = Queue()
        queue.enqueue([user_id])

        while queue.size() > 0:
            path_to_current_user = queue.dequeue()
            current_user = path_to_current_user[-1]
            if current_user not in visited:
                visited[current_user] = path_to_current_user
                for friend in self.friendships[current_user]:
                    path_to_friend = [*path_to_current_user, friend]
                    queue.enqueue(path_to_friend)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
