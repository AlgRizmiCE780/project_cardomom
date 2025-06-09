import os
import requests
import argparse

def remove_background(image_path, api_key, output_directory):
    # API endpoint
    url = "https://api.remove.bg/v1.0/removebg"

    # Set the API key as a header
    headers = {
        "X-Api-Key": "yGbxCvyEKVMYtoyRX4P7hCYh"
    }

    # Open the image file in binary mode
    with open(image_path, "rb") as image_file:
        # Send a POST request to the API
        response = requests.post(url, headers=headers, files={"image_file": image_file})

        # Save the output image file
        if response.status_code == requests.codes.ok:
            # Create the output directory if it doesn't exist
            os.makedirs(output_directory, exist_ok=True)

            # Determine the output image file path
            image_name = os.path.splitext(os.path.basename(image_path))[0]
            output_image_path = os.path.join(output_directory, f"{image_name}_output.png")

            with open(output_image_path, "wb") as output_file:
                output_file.write(response.content)
                print(f"Background removed successfully. Output saved as {output_image_path}")
        else:
            print(f"Error: {response.status_code}, {response.content.decode('utf-8')}")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Remove background from a set of images using remove.bg API")
    parser.add_argument("input_directory", type=str, help="D:/project_cardomom/Test_images")
    parser.add_argument("api_key", type=str, help="yGbxCvyEKVMYtoyRX4P7hCYh")
    parser.add_argument("output_directory", type=str, help="D:/project_cardomom/output")
    args = parser.parse_args()

    # Process each image in the input directory
    for filename in os.listdir(args.input_directory):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_path = os.path.join(args.input_directory, filename)
            remove_background(image_path, args.api_key, args.output_directory)

if __name__ == "__main__":
    main()
