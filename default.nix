{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.texlive.combined.scheme-full  # 这个包含了 ctex 和大多数需要的包
  ];
}
