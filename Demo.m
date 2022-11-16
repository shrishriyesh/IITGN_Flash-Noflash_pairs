%Demo
clear all
close all
clc
%image 1
% no_flash='image1_noflash.bmp';
% flash='image1_flash.bmp';
% A=imread(no_flash);
% F=imread(flash);
% out=FNF(F,A,'image1',9,4,0.1,-25); 

% %image 2
% no_flash='image2_noflash.bmp';
% flash='image2_flash.bmp';
% A=imread(no_flash);
% F=imread(flash);
% out=FNF(F,A,'image2',17,3,0.15,-50); 

% image 3
% no_flash='image3_noflash.bmp';
% flash='image3_flash.bmp';
% A=imread(no_flash);
% F=imread(flash);
% out=FNF(F,A,'image3',19,3,1.1,-22); 

% image 4
% no_flash='image4_noflash.bmp';
% flash='image4_flash.bmp';
% A=imread(no_flash);
% F=imread(flash);
% out=FNF(F,A,'image4',15,5,1.1,-35); 

%image 5
no_flash='TestA.png';
flash='TestF.png';
A=imread(no_flash);
F=imread(flash);
out=FNF(F,A,'image5',15,5,0.35,-55); 

figure;imshow(A);title('no flash');
figure;imshow(F);title('flash');
figure;imshow(out);title('result');
