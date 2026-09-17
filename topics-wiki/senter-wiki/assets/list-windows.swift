// list on-screen windows (id, owner, name, bounds) — used to find the Dock's "Desktop Picture" window
// run: swift assets/list-windows.swift
import Foundation
import CoreGraphics
let opts: CGWindowListOption = [.optionOnScreenOnly]
if let list = CGWindowListCopyWindowInfo(opts, kCGNullWindowID) as? [[String: Any]] {
    for w in list {
        let id = w[kCGWindowNumber as String] as? Int ?? -1
        let owner = w[kCGWindowOwnerName as String] as? String ?? ""
        let name = w[kCGWindowName as String] as? String ?? ""
        let layer = w[kCGWindowLayer as String] as? Int ?? 0
        let b = w[kCGWindowBounds as String] as? [String: Any] ?? [:]
        print("\(id)\t\(layer)\t\(owner)\t\(name)\t\(b["X"] ?? 0),\(b["Y"] ?? 0) \(b["Width"] ?? 0)x\(b["Height"] ?? 0)")
    }
}
