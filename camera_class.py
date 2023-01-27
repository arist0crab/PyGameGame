class Camera:

    """Realizing camera class to fix it on the player"""

    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):

        """Move obj on camera dx and dy"""

        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def zero(self, obj):

        """Move obj on camera dx and dy"""

        obj.rect.x -= self.dx
        obj.rect.y -= self.dy

    def update(self, target, screen_size):

        """Fix camera on target"""

        self.dx = -(target.rect.x + target.rect.w // 2 - screen_size[0] // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - screen_size[1] // 2)

