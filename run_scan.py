from twainhandle.scantwain import ScanManager
import twain

if __name__ == "__main__":
    # ss = ScanManager()
    # ss.acquire_images()
    twain.acquire("scans/tt.bmp", ds_name=bytes(ScanManager.get_available()
                                                [0], "utf-8"), dpi=50, pixel_type="bw")
