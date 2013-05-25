.class public Lcom/example/demo/MainActivity;
.super Landroid/app/Activity;
.source "MainActivity.java"


# instance fields
.field private mAddAccountButton:Landroid/widget/Button;


# direct methods
.method public constructor <init>()V
    .locals 0

    .prologue
    .line 14
    invoke-direct {p0}, Landroid/app/Activity;-><init>()V

    return-void
.end method


# virtual methods
.method protected launchContactAdder()V
    .locals 2

    .prologue
    .line 31
    new-instance v0, Landroid/content/Intent;

    const-class v1, Lcom/example/demo/a1;

    invoke-direct {v0, p0, v1}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    .line 32
    .local v0, i:Landroid/content/Intent;
    invoke-virtual {p0, v0}, Lcom/example/demo/MainActivity;->startActivity(Landroid/content/Intent;)V

    .line 33
    return-void
.end method

.method protected onCreate(Landroid/os/Bundle;)V
    .locals 2
    .parameter "savedInstanceState"

    .prologue
    .line 19
    invoke-super {p0, p1}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V

    .line 20
    const v0, 0x7f030001

    invoke-virtual {p0, v0}, Lcom/example/demo/MainActivity;->setContentView(I)V

    .line 22
    iget-object v0, p0, Lcom/example/demo/MainActivity;->mAddAccountButton:Landroid/widget/Button;

    new-instance v1, Lcom/example/demo/MainActivity$1;

    invoke-direct {v1, p0}, Lcom/example/demo/MainActivity$1;-><init>(Lcom/example/demo/MainActivity;)V

    invoke-virtual {v0, v1}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    .line 28
    return-void
.end method
