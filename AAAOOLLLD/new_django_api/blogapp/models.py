from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_img", blank=True, null=True)
    facebook = models.URLField(max_length=255, blank=True, null=True)
    youtube = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    twitter = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username


class Blog(models.Model):
    CATEGORY = (
        ("Technology", "Technology"),
        ("Economy", "Economy"),
        ("Business", "Business"),
        ("Sports", "Sports"),
        ("Lifestyle", "Lifestyle"),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="blogs",
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True, db_index=True)
    is_draft = models.BooleanField(default=True)
    category = models.CharField(max_length=50, choices=CATEGORY, blank=True, null=True)
    featured_image = models.ImageField(upload_to="blog_img", blank=True, null=True)

    class Meta:
        ordering = ["-published_date", "-created"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Ensure slug fits into max_length and is unique.
        max_len = Blog._meta.get_field("slug").max_length
        base_slug = slugify(self.title) if self.title else "post"
        # Truncate base_slug to max_len (so suffix logic has room)
        if len(base_slug) > max_len:
            base_slug = base_slug[:max_len]

        if not self.slug:
            slug = base_slug
            num = 2
            # ensure unique slug excluding self (for updates)
            while Blog.objects.exclude(pk=self.pk).filter(slug=slug).exists():
                suffix = f"-{num}"
                # ensure truncated base + suffix <= max_len
                trunc_len = max_len - len(suffix)
                if trunc_len <= 0:
                    # fallback: use numeric-only slug (should be extremely rare)
                    slug = slugify(base_slug)[: max_len - len(suffix)] + suffix
                else:
                    slug = f"{base_slug[:trunc_len]}{suffix}"
                num += 1
            self.slug = slug

        # If the post is being published (is_draft changed to False) and no published_date set, set it.
        # We can't easily compare previous value without an extra DB fetch; only set when published_date is empty.
        if not self.is_draft and self.published_date is None:
            self.published_date = timezone.now()

        super().save(*args, **kwargs)
