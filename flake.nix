{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    {
      self,
      nixpkgs,
    }:
    let
      lib = nixpkgs.lib;
      pkgs = import nixpkgs {
        system = "x86_64-linux";
        config.allowUnfreePredicate = pkg: builtins.elem (lib.getName pkg) [ "vscode" ];
      };
    in
    {
      devShells."x86_64-linux".default = pkgs.mkShell {
        packages = with pkgs; [
          (pkgs.python312.withPackages (
            python-pkgs: with python-pkgs; [
              #####################
              # Development tools #
              #####################

              pip
              virtualenv

              # IDE features / LSP
              python-lsp-server
              # pyls-isort # sort input
              # python-lsp-black # format code with black
              python-lsp-ruff # lint code with ruff

              # Formatting / Linting
              # black
              # autopep8
              # ruff
              # pylint
              # yapf
            ]
          ))

          nodePackages.prettier
        ];

        DJANGO_SETTINGS_MODULE = "oursite.settings";

        shellHook = ''
          export PYTHONPATH="$PWD"
        '';
      };
    };
}
