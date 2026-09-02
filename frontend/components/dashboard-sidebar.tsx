"use client";
import Link from "next/link";
import { MessageSquare, Users, Bot, Settings, Home, BarChart2, Zap, Clock } from "lucide-react";
import { usePathname } from "next/navigation";

const navItems = [
  { name: "Dashboard", href: "/dashboard", icon: Home },
  { name: "Inbox", href: "/dashboard/inbox", icon: MessageSquare },
  { name: "Customers", href: "/dashboard/customers", icon: Users },
  { name: "Analytics", href: "/dashboard/analytics", icon: BarChart2 },
  { name: "Automations", href: "/dashboard/automations", icon: Zap },
  { name: "AI Settings", href: "/dashboard/ai", icon: Bot },
  { name: "Business Hours", href: "/dashboard/business-hours", icon: Clock },
  { name: "Settings", href: "/dashboard/settings", icon: Settings },
];

export function DashboardSidebar() {
  const pathname = usePathname();

  return (
    <div className="w-64 bg-background border-r flex flex-col h-screen">
      <div className="p-4 border-b font-bold text-xl">SupportAI</div>
      <nav className="flex-1 p-4 space-y-2">
        {navItems.map((item) => {
          const Icon = item.icon;
          const isActive = pathname === item.href;
          return (
            <Link
              key={item.href}
              href={item.href}
              className={`flex items-center gap-3 px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                isActive
                  ? "bg-primary text-primary-foreground"
                  : "text-muted-foreground hover:bg-secondary hover:text-foreground"
              }`}
            >
              <Icon className="w-4 h-4" />
              {item.name}
            </Link>
          );
        })}
      </nav>
    </div>
  );
}
