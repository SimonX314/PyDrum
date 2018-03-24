// First try of a drum membrane in Gmsh

// Points
Point(1) = {40.5, 0, 0, 1.0};
Point(2) = {40.5, 40.5, 0, 1.0};
Point(3) = {0, 40.5, 0, 1.0};
Point(4) = {40.5, 81, 0, 1.0};
Point(5) = {81, 40.5, 0, 1.0};

// Geometry
Circle(1) = {3, 2, 4};
Circle(2) = {4, 2, 5};
Circle(3) = {5, 2, 1};
Circle(4) = {1, 2, 3};
Line Loop(1) = {1, 2, 3, 4};
Plane Surface(1) = {1};

// Physical groups
Physical Line("contour") = {2, 1, 4, 3};
Physical Surface("membrane") = {1};
