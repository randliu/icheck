.class Lcom/example/demo/MainActivity$1;
.super Ljava/lang/Object;
.source "MainActivity.java"

# interfaces
.implements Landroid/view/View$OnClickListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/example/demo/MainActivity;->onCreate(Landroid/os/Bundle;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/example/demo/MainActivity;


# direct methods
.method constructor <init>(Lcom/example/demo/MainActivity;)V
    .locals 0
    .parameter

    .prologue
    .line 1
    iput-object p1, p0, Lcom/example/demo/MainActivity$1;->this$0:Lcom/example/demo/MainActivity;

    .line 22
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 2
    .parameter "v"

    .prologue
    .line 24
    const-string v0, "fd"

    const-string v1, "mAddAccountButton clicked"

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 25
    iget-object v0, p0, Lcom/example/demo/MainActivity$1;->this$0:Lcom/example/demo/MainActivity;

    invoke-virtual {v0}, Lcom/example/demo/MainActivity;->launchContactAdder()V

    .line 26
    return-void
.end method
