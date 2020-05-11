class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        self.fill(image, sr, sc, image[sr][sc], newColor)
        return image


    def fill(self, image, r, c, old_color, new_color):
        image[r][c] = new_color
        if r > 0 and image[r - 1][c] == old_color:
            self.fill(image, r - 1, c, old_color, new_color)
        if r < len(image) - 1 and image[r + 1][c] == old_color:
            self.fill(image, r + 1, c, old_color, new_color)
        if c > 0 and image[r][c - 1] == old_color:
            self.fill(image, r, c - 1, old_color, new_color)
        if c < len(image[0]) - 1 and image[r][c + 1] == old_color:
            self.fill(image, r, c + 1, old_color, new_color)