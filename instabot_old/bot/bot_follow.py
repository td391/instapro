from tqdm import tqdm

from . import limits
from . import delay


def follow(self, user_id):
    user_id = self.convert_to_user_id(user_id)
    if not self.check_user(user_id):
        return True
    if limits.check_if_bot_can_follow(self):
        delay.follow_delay(self)
        if super(self.__class__, self).follow(user_id):
            self.User.counters.follows += 1
            self.User.following.append(user_id)
            return True
    else:
        self.logger.info("Out of follows for today.")
    return False


def follow_users(self, user_ids):
    broken_items = []
    user_ids = self.prefilter_users_to_follow(user_ids)
    for user_id in tqdm(user_ids, desc="Following users"):
        if not self.follow(user_id):
            delay.error_delay(self)
            broken_items = user_ids[user_ids.index(user_id):]
            break
    self.logger.info("DONE: Total followed %d users." %
                     self.User.counters.follows)
    return broken_items


def follow_followers(self, user_id, nfollows=None):
    self.logger.info("Follow followers of: %s" % user_id)
    if not user_id:
        self.logger.info("User not found.")
        return
    follower_ids = self.get_user_followers(user_id)
    if not follower_ids:
        self.logger.info("%s not found / closed / has no followers." % user_id)
    else:
        self.follow_users(follower_ids[:nfollows])


def follow_following(self, user_id, nfollows=None):
    self.logger.info("Follow following of: %s" % user_id)
    if not user_id:
        self.logger.info("User not found.")
        return
    following_ids = self.get_user_following(user_id)
    if not following_ids:
        self.logger.info("%s not found / closed / has no following." % user_id)
    else:
        self.follow_users(following_ids[:nfollows])