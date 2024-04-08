import unittest
from project.social_media import SocialMedia


class TestSocialMedia(unittest.TestCase):
    def setUp(self):
        self.user_instagram = SocialMedia("user_insta", "Instagram", 5000, "photo")
        self.user_youtube = SocialMedia("user_yt", "YouTube", 10000, "video")

    def test_platform_validity(self):
        with self.assertRaises(ValueError):
            self.user_invalid_platform = SocialMedia("user_invalid", "Invalid", 2000, "text")

    def test_valid_platform_init(self):
        self.assertEqual("Instagram", self.user_instagram.platform)
        self.assertEqual("user_yt", self.user_youtube._username)
        self.assertEqual(10000, self.user_youtube.followers)
        self.assertEqual("video", self.user_youtube._content_type)

    def test_followers_non_negative(self):
        with self.assertRaises(ValueError) as ve:
            self.user_negative_followers = SocialMedia("user_negative", "Instagram", -2000, "photo")

        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_create_post(self):
        self.assertEqual(self.user_instagram.create_post("A beautiful photo"),
                         "New photo post created by user_insta on Instagram.")
        self.assertEqual(self.user_youtube.create_post("An interesting video"),
                         "New video post created by user_yt on YouTube.")

    def test_like_post(self):
        self.user_instagram.create_post("A beautiful photo")
        self.assertEqual(self.user_instagram.like_post(0), "Post liked by user_insta.")

        for _ in range(10):
            self.user_instagram.like_post(0)
        self.assertEqual(self.user_instagram.like_post(0), "Post has reached the maximum number of likes.")

    def test_comment_on_post(self):
        self.user_youtube.create_post("An interesting video")
        self.assertEqual(self.user_youtube.comment_on_post(0, "Great video!"),
                         "Comment added by user_yt on the post.")
        self.assertEqual(self.user_youtube.comment_on_post(0, "Short"), "Comment should be more than 10 characters.")


if __name__ == '__main__':
    unittest.main()
