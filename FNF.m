function out = FNF( F,A ,fileName, n, sigma1, sigma2,T)
%FNF function: performs flash/no-flash algorithm for denoising using
%flash/no-flash image pairs.

%Usage:
%   result=FNF(flash_image,no_flashimage);
%   result=FNF(flash_image,no_flashimage,'output',5,3,0.2,-15);

%Input:
%   -F: flash image
%   -A: no-flash image
%   -fileName: the name of output file
%   -n: kernel size [nxn] should be odd number (default = 5)
%   -sigma1: space domain sigma (default = 3)
%   -sigma2: range domain sigma (default = 0.2)
%   -T: threshold of shadow mask (default = -10)

%Output:
%   -out: output image

%Citation:
%Petschnigg, Georg, et al. "Digital photography with flash and no-flash
%image pairs." ACM transactions on graphics (TOG) 23.3 (2004): 664-672.

%Author: Mahmoud Afifi, York University.

%argument's check
if nargin<2
    error('Too few input arguments');
elseif nargin<3
    n=5;
    sigma1=3;
    sigma2=0.2;
    fileName='output';
    T=-10;
elseif nargin<4
    n=5;
    sigma1=3;
    sigma2=0.2;
    T=-10;
elseif nargin<5
    sigma1=3;
    sigma2=0.2;
    T=-10;
elseif nargin<6
    sigma2=0.2;
    T=-10;
elseif nargin<7
    T=-10;
end

%kernel size check
if mod(n,2)==0
    error('Please use odd number for kernel size');
end
%dimensionality check
if size(A,1)~=size(F,1) || size(A,2)~=size(F,2) || ...
        size(A,3)~=size(F,3)
    error('Both images should have the same dimensions and number of color channels');
end

%create the mask
eps=0.02; %details eps (to avoid dividng by zero)
if size(A,3)>1
    gA=double(rgb2gray(A));
    gF=double(rgb2gray(F));
else
    gA=double(A);
    gF=double(F);
end
mf=zeros(size(A,1),size(A,2)); %initialization of shadow mask
ms=zeros(size(A,1),size(A,2)); %initialization of specularitiy mask
diff=gF-gA; 
mf(diff<=T)=1; %detect shadow
ms((gF/max(gF(:)))>0.95)=1; %detect specularities

M=zeros(size(A,1),size(A,2),size(A,3)); %initialization of mask
 se= strel('disk',2);
for i=1:size(A,3) %build the flash mask
    m=mf|ms; %merge two masks
    M(:,:,i) = imdilate(m,se);
end
display('calculate A_base...');
A_base=double(bfilter2(A,A,n,sigma1,sigma2));
display('calculate A_NR...');
A_nr=double(bfilter2(A,F,n,sigma1,sigma2));
display('calculate F_Base...');
F_base=double(bfilter2(F,F,n,sigma1,sigma2));
display('calculate F_Details...');
F_details=(double(F)+eps)./(double(F_base)+eps);
display('almost done..!');
out=uint8((1-M).*A_nr.*F_details+M.*A_base);


%save images
imwrite(A_base/255,strcat(fileName,'_Base.bmp'));
imwrite(A_nr/255,strcat(fileName,'_NR.bmp'));
imwrite(F_details,strcat(fileName,'_Details.bmp'));
imwrite(M(:,:,1),strcat(fileName,'_Mask.bmp'));
imwrite(out,strcat(fileName,'_Output.bmp'));
end

