import pytest
from PIL import Image
from image_processor import crop_image, add_watermark

@pytest.fixture
def sample_image():
  """Creates a 200x100 red image for testing."""
  return Image.new('RGB', (200, 100), color='red')

def test_crop_image_square(sample_image):
  """Test cropping to 1:1 aspect ratio."""
  # Original is 200x100.
  # 1:1 fit means height stays 100, width becomes 100.
  cropped = crop_image(sample_image, "1:1")
  assert cropped.size == (100, 100)

def test_crop_image_widescreen(sample_image):
  """Test cropping to 16:9 aspect ratio."""
  # Original 200x100 (Ratio 2.0). Target 16:9 (Ratio ~1.77).
  # Image is wider than target. Height should stay 100.
  # New Width = 100 * (16/9) = ~177.
  cropped = crop_image(sample_image, "16:9")
  
  assert cropped.size[1] == 100
  # Allow slight rounding differences
  assert 176 <= cropped.size[0] <= 178

def test_crop_invalid_ratio(sample_image):
  """Test that invalid input returns the original image safely."""
  # Should log an error and return original image
  cropped = crop_image(sample_image, "invalid-ratio")
  assert cropped.size == sample_image.size

def test_add_watermark_execution(sample_image):
  """Test that watermarking returns a valid image object."""
  watermarked = add_watermark(sample_image, "Test Watermark")
  
  # Check we got an image back
  assert isinstance(watermarked, Image.Image)
  # Size should remain unchanged
  assert watermarked.size == sample_image.size
  # Mode should be RGBA because watermark adds transparency layer
  assert watermarked.mode == "RGBA"