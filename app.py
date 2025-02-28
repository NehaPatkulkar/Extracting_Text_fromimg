import os
from textExtraction import extract_text


def main():
    dataset_path = r"C:\Users\Admin\Desktop\image dataset\data_subset\data_subset"

    # Check if dataset path exists
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset path '{dataset_path}' not found.")
        return

    # Get a list of image files
    image_files = [f for f in os.listdir(dataset_path) if f.lower().endswith((".jpg", ".png", ".jpeg"))]

    # Process only the first 5 images
    for filename in image_files[:5]:
        image_path = os.path.join(dataset_path, filename)

        try:
            text = extract_text(image_path)
            print(f"\n📌 Extracted Text from {filename}:\n{text}\n")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    main()
