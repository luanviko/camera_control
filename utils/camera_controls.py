from dataclasses import dataclass
import subprocess, sys


@dataclass
class Camera:
    """Class representing a camera connected via gphoto2.

    Attributes:
        port: Camera port address as string.
    """
    port: str

    def __run_gcode(self, args: list[str]) -> subprocess.CompletedProcess[str]:
        """Runs gphoto2 command with given arguments.

        Args:
            args: List of command arguments.

        Returns:
            Completed process result from subprocess.run().
        """
        arguments = " ".join(args)
        command = f"gphoto2 --port {self.port} {arguments}"
        return subprocess.run(
            command, 
            capture_output=True,
            text=True,
            shell=True
        )

    def print_return(self, ret: subprocess.CompletedProcess[str]) -> None:
        """Prints command output to appropriate streams.

        Args:
            ret: Completed process result to print.
        """
        print(ret.stdout, end="")
        if ret.stderr:
            print(ret.stderr, end="", file=sys.stderr)

    def get_config(self, entry: str) -> subprocess.CompletedProcess[str]:
        """Gets camera configuration for specified entry.

        Args:
            entry: Configuration entry path (e.g. '/main/imgsettings/iso').

        Returns:
            Completed process with configuration data.
        """
        return self.__run_gcode(["--get-config", entry])

    def get_current_config(self, entry: str) -> str:
        """Gets current value of a configuration entry.

        Args:
            entry: Configuration entry path.

        Returns:
            Current value as string, or empty string on error.
        """
        ret = self.__run_gcode(["--get-config", entry])
        if ret.stderr:
            print(ret.stderr, end="", file=sys.stderr)
            return ""
        return ret.stdout.split("\n")[3].replace("Current: ", "")

    def set_config(self, entry: str, value: str) -> subprocess.CompletedProcess[str]:
        """Sets camera configuration value.

        Args:
            entry: Configuration entry path.
            value: Value to set.

        Returns:
            Completed process result.
        """
        return self.__run_gcode(["--set-config", f'{entry}="{value}"'])
        
    def list_iso(self) -> subprocess.CompletedProcess[str]:
        """Lists available ISO values.

        Returns:
            Completed process with ISO options.
        """
        return self.get_config("/main/imgsettings/iso")

    def list_shutterspeed(self) -> subprocess.CompletedProcess[str]:
        """Lists available shutter speeds.

        Returns:
            Completed process with shutter speed options.
        """
        return self.get_config("/main/capturesettings/shutterspeed")

    def get_iso(self) -> str:
        """Gets current ISO setting.

        Returns:
            Current ISO value as string.
        """
        return self.get_current_config("/main/imgsettings/iso")

    def get_shutterspeed(self) -> str:
        """Gets current shutter speed.

        Returns:
            Current shutter speed value as string.
        """
        return self.get_current_config("/main/capturesettings/shutterspeed")

    def change_iso(self, choice: str) -> subprocess.CompletedProcess[str]:
        """Changes camera ISO setting.

        Args:
            choice: ISO choice to set. Refer to documentation for ISO value/choice correspondance.

        Returns:
            Completed process result.
        """
        return self.set_config("/main/imgsettings/iso", choice)

    def change_shutterspeed(self, choice: str) -> subprocess.CompletedProcess[str]:
        """Changes camera shutter speed.

        Args:
            choice: Shutter speed choice to set. Refer to documentation for value/choice correspondance.

        Returns:
            Completed process result.
        """
        return self.set_config("/main/capturesettings/shutterspeed", choice)

    def list_config(self) -> subprocess.CompletedProcess[str]:
        """Lists basic configuration options for a camera.

        Returns:
            Completed process result with configuration list.
        """
        return self.__run_gcode(["--list-config"])

    def capture_photo(self, photo_dir:str, prefix:str, debug:bool = False) -> subprocess.CompletedProcess[str]:
        args = [
            '--capture-image-and-download', 
            f'--filename={photo_dir}/{prefix}_%Y-%m-%d-T%H%M%S.%C'
        ]
        return self.__run_gcode(args)

@dataclass
class gphoto2:
    """Wrapper for gphoto2 command-line interface operations."""

    def run_gcode(self, args: list[str]) -> subprocess.CompletedProcess[str]:
        """Executes a gphoto2 command with the given arguments.

        Args:
            args: List of command-line arguments for gphoto2.

        Returns:
            Completed process result from subprocess.run().
        """
        return subprocess.run(
            f"gphoto2 {' '.join(args)}",
            capture_output=True,
            text=True,
            shell=True
        )

    def auto_detect(self) -> subprocess.CompletedProcess[str]:
        """Detects connected cameras automatically.

        Returns:
            Completed process result with detection output.
        """
        return self.run_gcode(["--auto-detect"])

    def list_all_config(self, port: str) -> subprocess.CompletedProcess[str]:
        """Lists all available configuration options for a camera.

        Args:
            port: Camera port address (e.g. 'usb:001,002').

        Returns:
            Completed process result with configuration list.
        """
        return self.run_gcode([f"--port {port}", "--list-all-config"])

    def list_config(self, port: str) -> subprocess.CompletedProcess[str]:
        """Lists basic configuration options for a camera.

        Args:
            port: Camera port address.

        Returns:
            Completed process result with configuration list.
        """
        return self.run_gcode([f"--port {port}", "--list-config"])

    def print_return(self, ret: subprocess.CompletedProcess[str]) -> None:
        """Prints command output to appropriate streams.

        Args:
            ret: Completed process result to print.
        """
        print(ret.stdout, end="")
        if ret.stderr:
            print(ret.stderr, end="", file=sys.stderr)