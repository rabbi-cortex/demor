import { LucideIcon } from "lucide-react";
import { cn } from "@/lib/utils";

interface CardProps {
  title: string;
  value: string;
  icon?: LucideIcon;
}

export function DashboardCard({ title, value, icon: Icon }: CardProps) {
  return (
    <div className="bg-card p-6 rounded-xl border border-border">
      <div className="flex justify-between items-start">
        <h3 className="text-sm text-foreground/70">{title}</h3>
        {Icon && <Icon className="w-5 h-5 text-primary" />}
      </div>
      <p className="text-3xl font-bold mt-2">{value}</p>
    </div>
  );
}
