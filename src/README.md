# src

### Rubiks_Cube
Contains the class structure for the Rubik's Cube.

### Rubiks_Cube_Reader
Activates the webcam, overlays a bounding box, and collects the images of the actual mixed Rubik's Cube.

### Rubiks_Cube_Solver
Finds and prints the solution to the Rubik's Cube given an input of the color matrix, which is the output of the Rubiks_Cube_Reader.

### Rubiks_Cube_Synthesizer
To train the CNN, many images of a Rubik's Cube would need to be fed into the model along with an array of the color labels of the cubies on the face (e.g. [blue, green, red, red, red, orange, yellow, white, white]). Rather than spending lots of time sitting in front of the webcam and taking images, I've attempted to implement a script that synthesizes RGB arrays along with their label arrays of what a Rubik's Cube may look like to use as the dataset. I've set the color scheme to use randomized shades of the 6 Rubik's Cube colors to account for differences in cubes, webcams, lighting, etc.