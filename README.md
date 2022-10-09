<h1>Python Freeform Gradient (Inspired by Clip Studio Paint)</h1>
<h3>Note: I'm just lerping colors here, have no idea how the freeform algorithm works</h3>



**Requirements:**

- Python version: 3.9.0

- Numpy

- OpenCV

- Pillow

---

  **Use pip to install the requirements automatically**

```python
pip install -r requirements.txt
```

---

**Usage**:

Open `main.py` with any text editor, scroll down to `line 19` and change `IN_IMAGE_NAM` to your Image name. *(Image file should be in the same directory as `main.py`)*

Then run the following in [Windows Terminal](https://github.com/microsoft/terminal) *(For colored Debug prints)*

```python
python main.py
```

## Examples:

**Input #1**

<img title="Input Image 1" src="imgs\demo_10.png" alt="demo_10.png" width="256">

**Output #1**

<img title="Output Image 1" src="imgs\demo_10_UPDATED.png" alt="demo_10_UPDATED.png" width="256">

**Input #2**

<img title="Input Image 2" src="imgs\Face_Shadow_input.png" alt="Face_Shadow_input.png" width="316">

**Output #2**

<img title="Output Image 2" src="imgs\Face_Shadow_input_UPDATED.png" alt="Face_Shadow_input_UPDATED.png" width="340">

**Input #3**

<img title="Input Image 3" src="imgs\Pumpkin.png" alt="Pumpkin.png" width="316">

**Output #3**

<img title="Output Image 3" src="imgs\Pumpkin_UPDATED.png" alt="Pumpkin_UPDATED.png" width="340">
