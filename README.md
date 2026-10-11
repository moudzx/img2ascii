# img2ascii
Convert any image to ASCII art.

<table>
  <tr>
    <td>
      <img width="720" height="968" alt="portrait" src="https://github.com/user-attachments/assets/0fcabcd2-a7df-47ed-ac85-f2dd9a2ac7c7" />
    </td>
    <td>
      <img width="1632" height="1570" alt="Screenshot from 2026-10-11 08-56-02" src="https://github.com/user-attachments/assets/88529464-6cb3-43d4-a1a1-03a951fc1048" />
    </td>
  </tr>
</table>
 
## Usage
 
```bash
pip install pillow
python img2ascii.py photo.jpg
```
 
With options:
 
```bash
python img2ascii.py photo.jpg -w 90 -c 1.8 -o art.txt
```
 
| Flag | Long form | Default | Description |
|------|-----------|---------|-------------|
| `-w` | `--width` | `70` | Output width in characters |
| `-c` | `--contrast` | `1.5` | Contrast boost applied before conversion |
| `-i` | `--invert` | off | Flip brightness mapping for light backgrounds |
| `-o` | `--output` | `ascii.txt` | Output file path |
 
## Tips for good results
 
- Pick images with strong contrast and a clear subject.
- Crop tight on the subject.
- Remove the background first for a clean silhouette. The `rembg` package works well.
- Avoid busy or low-contrast images such as cluttered scenes. They turn into noise.
- Increase `-w` to 90 to 120 for more detail.
- Increase `-c` to 1.8 to 2.5 for sharper features.
- Add `-i` if the target background is light.

## License
MIT
