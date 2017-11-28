# UNITY BASICS

## Scene

### Perspective v Orthographic projections (2D button)

 In the Scene view’s control bar we have the **2D** button, that toggles the Scene view’s camera between perspective and orthographic projections.

 Toggling this setting has no effect on how your game finally appears when played – that’s determined by the camera(s) you set up in your scene – but it can be helpful when arranging objects.

 * Perspective: Objects appear smaller as they move further away from the camera. This projection type is used for developing 3D games.
 * Orthographic: in 2D mode, an object’s distance from the camera doesn’t affect its size. Therefore, an object that is further away from the camera will appear behind any closer objects, but its size will remain unchanged regardless of its position.

## Game Objects

### Pivot

A Sprite’s Pivot defines the origin of its local coordinate system. This point, for example, the Sprite’s Center or its Top Left corner, will be placed at the position defined by the GameObject’s Transform; rotations will occur around this point; and scaling will shrink or grow the Sprite from this point.

### Pixels To Units

For Sprites, Unity uses "Pixels Per Unit" to determine their unscaled size in units. This "unit" is a way to size your objects relative to each other, for example, assuming a scale such as 1 unit = 1 meter.

To determine the width, in "units", of a GameObject, you have to calculate it based on the "Pixels per Units" property of the Sprite, the image size (in pixels) and the desired scale, using the formula:

`ImageWidth / PixelsPerUnit * Scale = WidthInUnits`

For example, considering a Sprite imported from a 500 pixels wide image, a scale of 1.0 along the x-axis, and a value in Pixels Per Unit of 100, we have a width of 5.0:

`500 / 100 * 1.0 = 5.0`