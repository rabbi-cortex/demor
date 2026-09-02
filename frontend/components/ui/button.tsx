import React from "react";
import { Slot } from "@radix-ui/react-slot";
import { cn } from "@/lib/utils";

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary" | "outline";
  asChild?: boolean;
}

export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ variant = "primary", className = "", asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button";

    const baseClass = "inline-flex items-center justify-center rounded-lg text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 px-4 py-2";

    const variants = {
      primary: "bg-primary text-primary-foreground shadow hover:bg-primary/90",
      secondary: "bg-secondary text-secondary-foreground shadow-sm hover:bg-secondary/80",
      outline: "border border-input bg-background shadow-sm hover:bg-accent hover:text-accent-foreground",
    };

    const variantClass = variants[variant] || variants.primary;

    return (
      <Comp
        className={cn(baseClass, variantClass, className)}
        ref={ref}
        {...props}
      />
    );
  }
);
Button.displayName = "Button";
